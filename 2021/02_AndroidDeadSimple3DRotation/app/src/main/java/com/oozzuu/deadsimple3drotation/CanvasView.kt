package com.oozzuu.deadsimple3drotation

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Path
import android.graphics.PointF
import android.util.AttributeSet
import android.view.MotionEvent
import android.view.View

class CanvasView @JvmOverloads constructor(
    context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) {


    lateinit var v1: PointF
    lateinit var v2: PointF
    lateinit var v3: PointF
    val o: PointF = PointF(400f, 400f)

    init {
        v1 = PointF()
    }

    override fun onDraw(canvas: Canvas?) {
        super.onDraw(canvas)

        //val paint:Paint = Paint()


    }

    override fun onTouchEvent(event: MotionEvent?): Boolean {
        return super.onTouchEvent(event)
    }
}