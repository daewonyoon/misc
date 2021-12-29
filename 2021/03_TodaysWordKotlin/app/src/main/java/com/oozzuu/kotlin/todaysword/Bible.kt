package com.oozzuu.kotlin.todaysword

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

// room database
// https://latte-is-horse.tistory.com/155
@Entity(tableName = "bible")
data class Bible(
    @PrimaryKey(autoGenerate = true) val uid: Int?,
    @ColumnInfo val book: String?,
    @ColumnInfo val chapter: Int?,
    @ColumnInfo val verse: Int?,
    @ColumnInfo val text: String
)