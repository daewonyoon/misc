package com.oozzuu.kotlin.todolistbootcamp

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.oozzuu.kotlin.todolistbootcamp.databinding.ItemTodoBinding
import timber.log.Timber

class TodoAdapter(private val todos: List<Todo>) :
    RecyclerView.Adapter<TodoAdapter.TodoViewHolder>() {

    fun checkAll() {
        todos.forEach { it.completed = true }
        notifyDataSetChanged()
    }

    fun uncheckAll() {
        todos.forEach { it.completed = false }
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): TodoViewHolder {
        Timber.d("onCreateViewHolder")

        val binding = ItemTodoBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )

        return TodoViewHolder(binding).also { holder ->
            binding.completedCheckBox.setOnCheckedChangeListener { buttonView, isChecked ->
                Timber.d("checked clicked")
                todos.getOrNull(holder.adapterPosition)?.completed = isChecked
            }
        }
    }

    override fun onBindViewHolder(holder: TodoViewHolder, position: Int) {
        Timber.d("onBindViewHolder $position")
        holder.bind(todos[position])

    }

    override fun getItemCount(): Int = todos.size

    class TodoViewHolder(private val binding: ItemTodoBinding) :
        RecyclerView.ViewHolder(binding.root) {

        fun bind(todo: Todo) {
            binding.todoTitleText.text = todo.title
            binding.completedCheckBox.isChecked = todo.completed
        }
    }
}