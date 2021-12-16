package com.oozzuu.nlgokrapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.Response
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.oozzuu.nlgokrapp.databinding.ActivityMainBinding
import java.io.IOException

class MainActivity : AppCompatActivity() {

    private var queue: RequestQueue? = null
    private lateinit var binding: ActivityMainBinding
    var adapter : BookAdapter? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        queue = Volley.newRequestQueue(this)
        binding.rvResults.layoutManager = LinearLayoutManager(this)

        binding.btnSearch.setOnClickListener {
            sendRequest()
        }

    }

    fun buildParamString(): String {
        val params = HashMap<String, String>()
        val searchText = binding.editSearch.text.toString()

        params["page"] = "1"
        params["per_page"] = "100"
        params["collection_set"] = "1"
        params["sort_ksj"] = "SORT_TITLE ASC"
        params["search_field1"] = "total_field"
        params["value1"] = searchText.toString()

        val paramStrings: List<String> = params.toList()
            .map {
                Pair(
                    java.net.URLEncoder.encode(it.first, "utf-8"),
                    java.net.URLEncoder.encode(it.second, "utf-8")
                )
            }
            .map { "${it.first}=${it.second}" }
        val paramString: String = paramStrings.joinToString(separator = "&")

        //return java.net.URLEncoder.encode(paramString, "utf-8")
        return paramString
    }

    private fun sendRequest() {
        var url = binding.editUrl.text.toString()
        val searchText = binding.editSearch.text.toString()
        val paramString = buildParamString()

        url += "?"
        url += paramString

        val request =  StringRequest(
            Request.Method.GET, url,
            Response.Listener<String> { response ->
                binding.textviewResult.text = "Response is ${response}"
                processResponse(response)
            },
            Response.ErrorListener { response -> binding.textviewResult.text = "error : ${response}" }
        )
        queue?.add(request)

    }

    fun processResponse(response: String) {
        //val gson = Gson()
        //val boxOffice = gson.fromJson(response, BoxOffice::class.java)
        try {
            var parser = XmlPullParserHandler()
            val bookrecords = parser.parse(response.byteInputStream())

            //adapter?.listData?.clear()
            //adapter?.listData?.addAll(bookrecords)
            //adapter?.notifyDataSetChanged()
            binding.rvResults.adapter = BookAdapter(bookrecords)

        } catch (e: IOException) {
            e.printStackTrace()
        }
        //output1.append(response)
    }

}