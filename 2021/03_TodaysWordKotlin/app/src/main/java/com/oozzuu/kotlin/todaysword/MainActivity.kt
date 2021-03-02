package com.oozzuu.kotlin.todaysword

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val bible: List<String> =
            applicationContext.assets
                .open("개역한글판성경.utf8.txt")
                .bufferedReader()
                .use { it.readText() }
                .lines()

        button.setOnClickListener {
            textView.setText(bible.random())
        }
    }
}