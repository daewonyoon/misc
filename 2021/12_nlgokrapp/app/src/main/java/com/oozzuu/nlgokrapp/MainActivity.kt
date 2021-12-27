package com.oozzuu.nlgokrapp

import android.os.Bundle
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.oozzuu.nlgokrapp.databinding.ActivityMainBinding
import timber.log.Timber
import java.io.IOException

class MainActivity : AppCompatActivity() {

    private var queue: RequestQueue? = null
    private lateinit var binding: ActivityMainBinding
    private lateinit var adapter: BookAdapter
    private val viewModel: MyViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        queue = Volley.newRequestQueue(this)
        binding.rvResults.layoutManager = LinearLayoutManager(this)
        adapter = BookAdapter()
        binding.rvResults.adapter = adapter

        binding.btnSearch.setOnClickListener {
            sendRequest()
        }

        viewModel.booksLiveData.observe(
            this,
            {
                (binding.rvResults.adapter as BookAdapter).setData(it)
            })
    }

    private fun buildParamString(): String {
        val params = HashMap<String, String>()

        val searchText = binding.editSearch.text.toString()
        val searchAuthorText = binding.editSearch2.text.toString()
        val startYear = binding.editStartYear.text.toString()
        val endYear = binding.editEndYear.text.toString()

        params["page"] = "1"
        params["per_page"] = "1000"
        params["collection_set"] = "1" // 단행본
        params["sort_ksj"] = "SORT_TITLE ASC"
        params["search_field1"] = "total_field"
        params["value1"] = searchText
        if (searchAuthorText.isNotEmpty()) {
            params["and_or_not1"] = "AND"
            params["search_field2"] = "author"
            params["value2"] = searchAuthorText
        }
        if (startYear.isNotEmpty()) {
            params["start_year"] = startYear
        }
        if (endYear.isNotEmpty()) {
            params["end_year"] = endYear
        }

        val paramStrings: List<String> = params.toList()
            .map { "${url8encode(it.first)}=${url8encode(it.second)}" }

        return paramStrings.joinToString(separator = "&")
    }

    private fun url8encode(text: String): String? {
        return java.net.URLEncoder.encode(text, "utf-8")
    }

    private fun sendRequest() {
        var url = binding.editUrl.text.toString()
        val paramString = buildParamString()

        url += "?"
        url += paramString

        val request = StringRequest(
            Request.Method.GET, url,
            { response ->
                binding.textviewResult.text = "Response is ${response}"
                Timber.d("response : ${response}")
                processResponse(response)
            },
            { response ->
                binding.textviewResult.text = "error : ${response}"
                Timber.d("response error ${response}")
            }
        )
        queue?.add(request)
    }

    private fun processResponse(response: String) {
        try {
            val parser = XmlPullParserHandler()
            val bookRecords = parser.parse(response.byteInputStream())

            viewModel.clear()
            for (book in bookRecords) {
                viewModel.addBook(book)
            }

        } catch (e: IOException) {
            e.printStackTrace()
        }
        //output1.append(response)
    }
}