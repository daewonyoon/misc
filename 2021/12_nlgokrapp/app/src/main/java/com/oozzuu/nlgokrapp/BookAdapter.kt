package com.oozzuu.nlgokrapp

import android.text.Html
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.oozzuu.nlgokrapp.databinding.ItemBookBinding

// ref : https://cliearl.github.io/posts/android/viewbinding-recyclerview/
class BookAdapter : RecyclerView.Adapter<BookViewHolder>() {

    var listBook = mutableListOf<Book>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): BookViewHolder {
        val binding = ItemBookBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return BookViewHolder(binding)
    }

    override fun onBindViewHolder(holder: BookViewHolder, position: Int) {
        holder.bind(listBook[position])
    }

    override fun getItemCount(): Int {
        return listBook.size
    }
}

class BookViewHolder(private val binding: ItemBookBinding) : RecyclerView.ViewHolder(binding.root) {
    fun bind(book: Book) {
        binding.tvTitle.text = Html.fromHtml(book.title)
        binding.tvAuthor.text = Html.fromHtml(book.author)
        binding.tvContent.text = Html.fromHtml(book.content)
        binding.tvPublisher.text = Html.fromHtml(book.publisher)
        binding.tvPubyear.text = Html.fromHtml(book.pubYear)
        binding.tvLibname.text = Html.fromHtml(book.libName)
        binding.tvLibcode.text = Html.fromHtml(book.libCode)
    }
}
