package com.oozzuu.kotlin.todolistbootcamp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.oozzuu.kotlin.todolistbootcamp.databinding.ActivityMainBinding
import timber.log.Timber

class MainActivity : AppCompatActivity() {


    private lateinit var binding: ActivityMainBinding

    private val todos = listOf(
        Todo("make bootcamp youtube video #1", false),
        Todo("make bootcamp youtube video #2", false),
        Todo("make bootcamp youtube video #3", false),
        Todo("make bootcamp youtube video #4", false),
        Todo("make bootcamp youtube video #5", false),
        Todo("make bootcamp youtube video #6", false),
        Todo("make bootcamp youtube video #7", false),
        Todo("make bootcamp youtube video #8", false),
        Todo("make bootcamp youtube video #9", false),
        Todo("make bootcamp youtube video #10", false),
        Todo("make bootcamp youtube video #11", false),
        Todo("make bootcamp youtube video #12", false),
        Todo("make bootcamp youtube video #13", false),
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setupTimber()

        binding = ActivityMainBinding.inflate(layoutInflater)

        setContentView(binding.root)

        initializeViews()

    }

    private fun initializeViews() {
        binding.todoList.layoutManager = LinearLayoutManager(this)
        binding.todoList.adapter = TodoAdapter(todos)
        //binding.todoList.layoutManager = LinearLayoutManager(this)
    }

    private fun setupTimber() {
        Timber.plant(Timber.DebugTree())
    }
}