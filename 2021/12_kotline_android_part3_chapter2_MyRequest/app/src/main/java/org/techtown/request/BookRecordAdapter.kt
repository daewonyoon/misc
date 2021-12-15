package org.techtown.request

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.item_book.view.*

class BookRecordAdapter: RecyclerView.Adapter<BookRecordViewHolder>() {

    var listData = mutableListOf<BookRecord>()
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): BookRecordViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_book, parent, false)
        return BookRecordViewHolder(view)
    }

    override fun onBindViewHolder(holder: BookRecordViewHolder, position: Int) {
        val bookRecord = listData.get(position)
        holder.setBookRecord(bookRecord)
    }

    override fun getItemCount(): Int {
        return listData.size
    }


}

class BookRecordViewHolder(itemView: View): RecyclerView.ViewHolder(itemView) {
    fun setBookRecord(bookRecord:BookRecord) {
        itemView.tv_title.text = bookRecord.title
        itemView.tv_author.text = bookRecord.author
        itemView.tv_pubyear.text = bookRecord.pubYear
        itemView.tv_content.text = bookRecord.content
    }
}