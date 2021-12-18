package com.oozzuu.nlgokrapp

import android.text.Html
import android.text.Spanned
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

    fun setData(data: ArrayList<Book>) {
        //listBook = data
        listBook.clear()
        listBook.addAll(data)
        notifyDataSetChanged()
    }
}

class BookViewHolder(private val binding: ItemBookBinding) : RecyclerView.ViewHolder(binding.root) {
    fun bind(book: Book) {
        binding.tvTitle.text = fromHtml(book.title)
        binding.tvAuthor.text = fromHtml(book.author)
        binding.tvContent.text = fromHtml(book.content)
        binding.tvPublisher.text = fromHtml(book.publisher)
        binding.tvPubyear.text = fromHtml(book.pubYear)
        binding.tvLibname.text = fromHtml(book.libName)
        binding.tvLibcode.text = book.libCode
    }

    private fun fromHtml(html: String): Spanned? {
        return Html.fromHtml(html, Html.FROM_HTML_MODE_LEGACY)
    }
}
