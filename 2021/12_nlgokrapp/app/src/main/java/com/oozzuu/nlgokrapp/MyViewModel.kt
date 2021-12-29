package com.oozzuu.nlgokrapp

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class MyViewModel : ViewModel() {
    val booksLiveData = MutableLiveData<List<Book>>()

    private val data = arrayListOf<Book>()

    fun addBook(book: Book) {
        data.add(book)
        booksLiveData.value = data
    }

    fun deleteBook(book: Book) {
        data.remove(book)
        booksLiveData.value = data
    }

    fun setBooks(books: List<Book>) {
        data.clear()
        data.addAll(books)
        booksLiveData.value = data
    }

    fun clear() {
        data.clear()
        booksLiveData.value = data
    }

}