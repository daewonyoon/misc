package com.oozzuu.kotlin.simplegame

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    //private var btnPlay: Button? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //btnPlay = findViewById<Button>("btnPlay")

        btnPlay.setOnClickListener {
            val intent = Intent(this, GameActivity::class.java)
            startActivity(intent)

        }
    }
}