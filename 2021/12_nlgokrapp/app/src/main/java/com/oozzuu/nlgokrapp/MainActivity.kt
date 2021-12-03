package com.oozzuu.nlgokrapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import com.android.volley.toolbox.Volley
import com.android.volley.RequestQueue
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.StringRequest

class MainActivity : AppCompatActivity() {

    var searchButton :Button ?= null
    var urlEdit:EditText ?= null
    var queue :RequestQueue ?= null
    var textView :TextView?= null
    var searchEdit:EditText ?= null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

         searchButton = findViewById<Button>(R.id.btnSearch)
         urlEdit = findViewById<EditText>(R.id.editUrl)

         textView = findViewById<TextView>(R.id.tvResult)
         searchEdit = findViewById<EditText>(R.id.editSearch)
        queue =  Volley.newRequestQueue(this)

        searchButton?.setOnClickListener {
            sendRequest()
        }

    }

    fun sendRequest() {
        val url = urlEdit?.text.toString()
        val searchText = searchEdit?.text.toString()

        val request = object:StringRequest(
            Request.Method.GET, url,
            Response.Listener<String> { response ->
                textView?.text = "Response is ${response}"
            },
            Response.ErrorListener { response -> textView?.text = "error : ${response}" }
        ) {
            override fun getParams():MutableMap<String, String> {
                val params = HashMap<String, String>()

                params["page"] = "1"
                params["per_page"] = "100"
                params["collection_set"] = "1"
                params["sort_ksj"] = "SORT_TITLE ASC"
                params["search_field1"] = "total_field"
                params["value1"] = searchText



                return params

            }
        }
        queue?.add(request)

    }
}