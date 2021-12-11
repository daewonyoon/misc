package com.oozzuu.kotlin.todolistbootcamp

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.oozzuu.kotlin.todolistbootcamp.databinding.ItemTodoBinding
import timber.log.Timber

class TodoAdapter(private val todos: List<Todo>): RecyclerView.Adapter<TodoAdapter.TodoViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): TodoViewHolder {
        Timber.d("onCreateViewHolder")

        return TodoViewHolder(ItemTodoBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        ))
    }

    override fun onBindViewHolder(holder: TodoViewHolder, position: Int) {
        Timber.d("onBindViewHolder")
        holder.bind(todos[position])

    }

    override fun getItemCount(): Int = todos.size

    class TodoViewHolder (private val binding:ItemTodoBinding): RecyclerView.ViewHolder(binding.root) {


        fun bind(todo:Todo) {
            binding.todoTitleText.text = todo.title
            binding.completedCheckBox.isChecked = todo.completed
        }
    }
}