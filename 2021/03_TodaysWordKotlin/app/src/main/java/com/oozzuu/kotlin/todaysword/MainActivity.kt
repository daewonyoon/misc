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
            binding.textView.text = bible.random()
        }
         /*
        val bible: List<Bible> = db.bibleDao().getAll()

        binding.button.setOnClickListener {
            binding.textView.text = bible.random().text
        }
         */

    }
}