package com.oozzuu.kotlin.todaysword

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.room.Room
import com.oozzuu.kotlin.todaysword.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val db = Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java,
            "bible.db"
        )
            // TODO: createFromAsset("database/bible_ko.db")
            .build()

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)


        val bible: List<String> =
            applicationContext.assets
                .open("개역한글판성경.utf8.txt")
                .bufferedReader()
                .use { it.readText() }
                .lines()


        binding.button.setOnClickListener {
            val parsed = parseLine(bible.random())
            val book = parsed[0]
            val ch = parsed[1]
            val ver = parsed[2]
            val text = parsed[3]

            binding.tvBookchver.text = "${book} ${ch}장 ${ver}절"
            binding.textView.text = text
        }
        /*
       val bible: List<Bible> = db.bibleDao().getAll()

       binding.button.setOnClickListener {
           binding.textView.text = bible.random().text
       }
        */

    }

    val booknameMap: HashMap<String, String> = hashMapOf(
        "창" to "창세기",
        "출" to "출애굽기",
        "레" to "레위기",
        "민" to "민수기",
        "신명,신" to "신명기",
        "수" to "여호수아",
        "삿" to "사사기",
        "룻" to "룻기",
        "삼상" to "사무엘상",
        "삼하" to "사무엘하",
        "왕상" to "열왕기상",
        "왕하" to "열왕기하",
        "대상" to "역대기상",
        "대하" to "역대기하",
        "스" to "에즈라",
        "느" to "느헤미야",
        "에" to "에스더",
        "욥" to "욥기",
        "시" to "시편",
        "잠" to "잠언",
        "전" to "전도서",
        "아" to "아가",
        "사" to "이사야",
        "렘" to "예레미야",
        "애" to "예레미야애가",
        "겔" to "에스겔",
        "단" to "다니엘",
        "호" to "호세아",
        "욜" to "요엘",
        "암" to "아모스",
        "옵" to "오바댜",
        "욘" to "요나",
        "미" to "미가",
        "나" to "나훔",
        "합" to "하박국",
        "습" to "스바냐",
        "학" to "학개",
        "슥" to "스가랴",
        "말" to "말라기",
        "마" to "마태복음",
        "막" to "마가복음",
        "눅" to "누가복음",
        "요" to "요한복음",
        "행" to "사도행전",
        "롬" to "로마서",
        "고전" to "고린도전서",
        "고후" to "고린도후서",
        "갈" to "갈라디아서",
        "엡" to "에베소서",
        "빌" to "빌립보서",
        "골" to "골로새서",
        "살전" to "데살로니가전서",
        "살후" to "데살로니가후서",
        "딤전" to "디모데전서",
        "딤후" to "디모데후서",
        "딛" to "디도서",
        "몬" to "빌레몬서",
        "히" to "히브리서",
        "약" to "야고보서",
        "벧전" to "베드로전서",
        "벧후" to "베드로후서",
        "요일" to "요한1서",
        "요이" to "요한2서",
        "요삼" to "요한3서",
        "유" to "유다서",
        "계" to "요한계시록"
    )

    private fun parseLine(line: String): List<String> {
        val regex = """([^\d]+)(\d+):(\d+) (.*)""".toRegex()
        val result = regex.find(line)
        val (book, ch, ver, text) = result!!.destructured

        val bookname = booknameMap[book] ?: book

        // TODO: book to full name
        return listOf(bookname, ch, ver, text)
    }
}