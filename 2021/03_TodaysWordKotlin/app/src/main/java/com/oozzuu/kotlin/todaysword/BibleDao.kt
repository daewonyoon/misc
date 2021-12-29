package com.oozzuu.kotlin.todaysword

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query

@Dao
interface BibleDao {
    @Query("Select * from bible")
    fun getAll(): List<Bible>

    @Insert
    fun insertBible(bible: Bible)

    @Query("Delete from bible")
    fun deleteAll()


}