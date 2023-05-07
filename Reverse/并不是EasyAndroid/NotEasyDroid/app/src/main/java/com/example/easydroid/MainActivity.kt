package com.example.noteasydroid

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.noteasydroid.databinding.ActivityMainBinding
import kotlin.experimental.xor

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        findViewById<Button>(R.id.button).setOnClickListener {
            findViewById<EditText>(R.id.input).let { check(it.text.toString()) }.let { if (it) "Right" else "Wrong" }.let {
                Toast.makeText(this, it, Toast.LENGTH_LONG).show()
            }
        }
    }

    private fun check(s: ByteArray): Boolean {
        return s.map { it.xor(66) }.zip(
            arrayOf<Byte>(
                54,
                40,
                33,
                54,
                36,
                57,
                9,
                114,
                54,
                115,
                43,
                44,
                29,
                3,
                44,
                6,
                48,
                114,
                43,
                38,
                29,
                49,
                113,
                33,
                23,
                48,
                43,
                22,
                59,
                63
            )
        ).all { it.first == it.second }
    }

    external fun check(s: String): Boolean

    companion object {
        init {
            System.loadLibrary("noteasydroid")
        }
    }
}