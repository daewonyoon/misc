package com.oozzuu.kotlin.rockpaperscissors

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import android.widget.Toast
import com.oozzuu.kotlin.rockpaperscissors.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)

        setContentView(binding.root)

        val textView = binding.helloText


        textView.setOnClickListener{
            Toast.makeText(this, "Hello world clicked", Toast.LENGTH_SHORT).show()
        }
    }
}