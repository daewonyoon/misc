package org.techtown.request

import org.xmlpull.v1.XmlPullParser
import org.xmlpull.v1.XmlPullParserException
import org.xmlpull.v1.XmlPullParserFactory
import java.io.InputStream

class XmlPullParserHandler {
    val bookRecords = ArrayList<BookRecord>()
    var bookRecord: BookRecord? = null
    var textView: String = ""

    fun parse(inputStream: InputStream): List<BookRecord> {
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
                        bookRecord = BookRecord()
                    }
                    XmlPullParser.TEXT -> textView = parser.text
                    XmlPullParser.END_TAG -> if (tagname.equals("record", ignoreCase = true)) {
                        // add employee object to list
                        bookRecord?.let { bookRecords.add(it) }
                    } else if (tagname.equals("title", ignoreCase = true)) {
                        bookRecord!!.title = textView
                    } else if (tagname.equals("author", ignoreCase = true)) {
                        bookRecord!!.author = textView
                    } else if (tagname.equals("publisher", ignoreCase = true)) {
                        bookRecord!!.publisher = textView
                    } else if (tagname.equals("pubyear", ignoreCase = true)) {
                        bookRecord!!.pubYear = textView
                    } else if (tagname.equals("type", ignoreCase = true)) {
                        bookRecord!!.type = textView
                    } else if (tagname.equals("cover_yn", ignoreCase = true)) {
                        bookRecord!!.coverYn = textView
                    } else if (tagname.equals("cover_url", ignoreCase = true)) {
                        bookRecord!!.coverUrl = textView
                    } else if (tagname.equals("content", ignoreCase = true)) {
                        bookRecord!!.content = textView
                    } else if (tagname.equals("lib_name", ignoreCase = true)) {
                        bookRecord!!.libName = textView
                    } else if (tagname.equals("lib_code", ignoreCase = true)) {
                        bookRecord!!.libCode = textView
                    } else if (tagname.equals("rec_key", ignoreCase = true)) {
                        bookRecord!!.recKey = textView
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
