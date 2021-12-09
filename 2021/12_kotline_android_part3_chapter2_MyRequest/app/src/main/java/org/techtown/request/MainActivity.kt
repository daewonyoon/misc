package org.techtown.request

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import kotlinx.android.synthetic.main.activity_main.input1
import kotlinx.android.synthetic.main.activity_main.output1
import kotlinx.android.synthetic.main.activity_main.requestButton
import kotlinx.android.synthetic.main.activity_main.searchText
import java.io.IOException

class BookRecord {
    var title:String = ""
    var author:String = ""
    var publisher:String = ""
    var pubYear:String = ""
    var type:String = ""
    var content:String = ""
    var libName:String = ""
    var libCode:String = ""
    var recKey:String = ""
}

class MainActivity : AppCompatActivity() {

    companion object {
        var requestQueue: RequestQueue? = null
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        requestQueue = Volley.newRequestQueue(applicationContext)

        requestButton.setOnClickListener {

            send()
        }
    }

    fun buildParamString(): String {
        val params = HashMap<String, String>()

        params["page"] = "1"
        params["per_page"] = "100"
        params["collection_set"] = "1"
        params["sort_ksj"] = "SORT_TITLE ASC"
        params["search_field1"] = "total_field"
        params["value1"] = searchText.text.toString()

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

    fun send() {
        var url = input1.text.toString()

        //val paramString = URLEncodedUtils.format(params, "utf-8")
        //  url += paramString
        val paramString = buildParamString()

        url += "?"
        url += paramString

        output1.text = ""

        output1.append("\n url=`${url}`\n")

        val request = StringRequest(
            Request.Method.GET,
            url,
            {
                output1.append("\n응답 -> ${it}")

                // 키사용초과 여부 확인
                //if (it.indexOf("faultInfo") > -1) {
                //    output1.append("키사용량이 초과되었다면 아래 사이트에 가입 후 키를 발급받아 그 키로 사용하세요.")
                //    output1.append("http://kobis.or.kr/kobisopenapi")
                //} else {
                processResponse(it)
                //}
            },
            {
                output1.append("\n에러 -> ${it.message}")
            }
        )

        //request.setShouldCache(false)
        requestQueue?.add(request)
        output1.append("요청함")
    }

    fun processResponse(response: String) {
        //val gson = Gson()
        //val boxOffice = gson.fromJson(response, BoxOffice::class.java)
        try {
            var parser = XmlPullParserHandler()

        } catch (e:IOException) {
            e.printStackTrace()
        }
        output1.append(response)
    }
}