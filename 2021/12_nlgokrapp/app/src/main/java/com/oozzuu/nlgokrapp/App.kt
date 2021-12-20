package com.oozzuu.nlgokrapp

import android.app.Application
import timber.log.Timber

// timber setting : https://youtu.be/lBimVsddT4A
class App : Application() {
    override fun onCreate() {
        super.onCreate()

        Timber.plant(Timber.DebugTree())
    }
}