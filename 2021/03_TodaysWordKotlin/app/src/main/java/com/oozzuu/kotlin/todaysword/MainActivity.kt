package com.oozzuu.kotlin.todaysword

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.room.Room
import com.oozzuu.kotlin.todaysword.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val db = Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java,
            "bible.db"
        )
            // TODO: createFromAsset("database/bible_ko.db")
            .build()

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)


        val bible: List<String> =
            applicationContext.assets
                .open("개역한글판성경.utf8.txt")
                .bufferedReader()
                .use { it.readText() }
                .lines()


        binding.button.setOnClickListener {
            val parsed = parseLine(bible.random())
            val book = parsed[0]
            val ch = parsed[1]
            val ver = parsed[2]
            val text = parsed[3]

            binding.tvBookchver.text = "${book} ${ch}장 ${ver}절"
            binding.textView.text = text
        }
        /*
       val bible: List<Bible> = db.bibleDao().getAll()

       binding.button.setOnClickListener {
           binding.textView.text = bible.random().text
       }
        */

    }

    private fun parseLine(line: String): List<String> {

        val regex = """([^\d]+)(\d+):(\d+) (.*)""".toRegex()
        val result = regex.find(line)
        val (book, ch, ver, text) = result!!.destructured

        // TODO: book to full name
        return listOf(book, ch, ver, text)
    }
}