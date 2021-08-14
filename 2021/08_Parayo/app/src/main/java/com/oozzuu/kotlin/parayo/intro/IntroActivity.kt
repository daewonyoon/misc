package com.oozzuu.kotlin.parayo.intro

import android.app.Activity
import android.os.Bundle
import org.jetbrains.anko.setContentView

class IntroActivity: Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val ui = IntroActivityUI()
        ui.setContentView(this)
    }
}