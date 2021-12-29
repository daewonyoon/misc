package com.oozzuu.kotlin.todaysword

import androidx.room.Database
import androidx.room.RoomDatabase

@Database(entities = [Bible::class], version = 1, exportSchema = false)
abstract class AppDatabase : RoomDatabase() {
    abstract fun bibleDao(): BibleDao
}