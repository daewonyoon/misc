package com.oozzuu.kotlin.parayo.intro

import android.app.Activity
import android.os.Bundle
import android.util.Log
import com.oozzuu.kotlin.parayo.api.ParayoApi
import kotlinx.coroutines.runBlocking
import org.jetbrains.anko.setContentView

class IntroActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val ui = IntroActivityUI()
        ui.setContentView(this)

        runBlocking {
            try {
                val response = ParayoApi.instance.hello()

                Log.d("IntroActivity", response.data) // BUILD ERROR : Type mismatch: inferred type is String? but String was expected
            } catch (e: Exception) {
                Log.e("IntroActivity", "Hello API 호출오류", e)
            }
        }
    }
}