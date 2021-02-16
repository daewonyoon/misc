package com.oozzuu.drawshape

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Path
import android.util.AttributeSet
import android.view.View



class CanvasView @JvmOverloads constructor(
    context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) {


    override fun onDraw(canvas: Canvas?) {
        super.onDraw(canvas)

        val paint:Paint = Paint()
        paint.setColor(Color.RED)
        paint.strokeWidth = 2f
        canvas?.drawLine(0f, 0f, 700f, 1000f, paint)


        paint.setColor(Color.BLUE)
        paint.strokeWidth = 12f
        paint.style = Paint.Style.STROKE
        canvas?.drawCircle(400f, 600f, 200f, paint)

        paint.setColor(Color.YELLOW)
        paint.strokeWidth = 22f
        paint.style = Paint.Style.FILL
        canvas?.drawCircle(400f, 600f, 200f, paint)

        val path: Path = Path()
        path.moveTo(700f, 400f)
        path.lineTo(1000f, 1400f)
        path.lineTo(200f, 1400f)
        path.close()
        paint.setColor(Color.BLACK)
        paint.strokeWidth = 32f
        paint.style = Paint.Style.STROKE
        canvas?.drawPath(path, paint)
        paint.setColor(Color.GREEN)
        paint.strokeWidth = 2f
        paint.style = Paint.Style.FILL
        canvas?.drawPath(path, paint)
    }
}