package com.oozzuu.nlgokrapp

import org.xmlpull.v1.XmlPullParser
import org.xmlpull.v1.XmlPullParserException
import org.xmlpull.v1.XmlPullParserFactory
import java.io.InputStream

class XmlPullParserHandler {
    val bookRecords = ArrayList<Book>()
    var bookRecord: Book? = null
    var textView: String = ""

    fun parse(inputStream: InputStream): ArrayList<Book> {
        try {
            val factory = XmlPullParserFactory.newInstance()
            factory.isNamespaceAware = true
            val parser = factory.newPullParser()
            parser.setInput(inputStream, null)
            var eventType = parser.eventType

            while (eventType != XmlPullParser.END_DOCUMENT) {
                val tagname = parser.name
                when (eventType) {
                    XmlPullParser.START_TAG -> if (tagname.equals("record", ignoreCase = true)) {
                        // create a new instance of employee
                        bookRecord = Book("mm")
                    }
                    XmlPullParser.TEXT -> textView = parser.text
                    XmlPullParser.END_TAG -> {

                        when(tagname.lowercase()) {
                            "record" -> bookRecord?.let{bookRecords.add(it)}
                            "title" -> bookRecord!!.title = textView
                            "author" -> bookRecord!!.author = textView
                            "publisher" -> bookRecord!!.publisher = textView
                            "pubyear" -> bookRecord!!.pubYear = textView
                            "type" -> bookRecord!!.type = textView
                            "cover_yn" -> bookRecord!!.coverYn = textView
                            "cover_url" -> bookRecord!!.coverUrl = textView
                            "content" -> bookRecord!!.content = textView.trim()
                            "lib_name" -> bookRecord!!.libName = textView
                            "lib_code" -> bookRecord!!.libCode = textView
                            "rec_key" -> bookRecord!!.recKey = textView
                        }

                    }

                    else -> {
                    }
                }
                eventType = parser.next()
            }
        } catch (e: XmlPullParserException) {

            e.printStackTrace()
        }
        return bookRecords
    }
}
