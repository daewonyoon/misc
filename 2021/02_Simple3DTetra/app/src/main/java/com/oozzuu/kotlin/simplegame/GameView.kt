package com.oozzuu.kotlin.simplegame

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.view.MotionEvent
import android.view.View

class GameView(context: Context) : View(context) {

    val paint: Paint
    var circleX: Float
    var circleY: Float

    var o: Vector3D
    var axis1: Vector3D
    var axis2: Vector3D
    var axis3: Vector3D
    var axisNo: Int = 0

    init {
        paint = Paint()
        paint.isFilterBitmap = true
        paint.isAntiAlias = true
        paint.strokeWidth = 4f
        paint.color = Color.BLUE
        circleX = 100f
        circleY = 100f

        o = Vector3D(0f, 0f, 0f)
        axis1 = Vector3D(1f, 0f, 0f)
        axis2 = Vector3D(0f, 1f, 0f)
        axis3 = Vector3D(0f, 0f, 1f)
    }

    override fun draw(canvas: Canvas?) {
        super.draw(canvas)

        canvas?.drawColor(Color.WHITE)
        //canvas?.drawCircle(circleX, circleY, 50f, paint)

        paint.color = Color.BLUE
        canvas?.drawLine(axis1.x_prj, axis1.y_prj, axis2.x_prj, axis2.y_prj, paint)
        paint.color = Color.RED
        canvas?.drawLine(axis2.x_prj, axis2.y_prj, axis3.x_prj, axis3.y_prj, paint)
        paint.color = Color.LTGRAY
        canvas?.drawLine(axis1.x_prj, axis1.y_prj, axis3.x_prj, axis3.y_prj, paint)
        paint.color = Color.GREEN
        canvas?.drawLine(axis1.x_prj, axis1.y_prj, o.x_prj, o.y_prj, paint)
        paint.color = Color.MAGENTA
        canvas?.drawLine(o.x_prj, o.y_prj, axis2.x_prj, axis2.y_prj, paint)
        paint.color = Color.BLACK
        canvas?.drawLine(o.x_prj, o.y_prj, axis3.x_prj, axis3.y_prj, paint)
    }

    override fun onTouchEvent(event: MotionEvent?): Boolean {
        //circleX = event!!.x
        //circleY = event!!.y
        when(event!!.action) {
            MotionEvent.ACTION_MOVE -> {

                rotate(axisNo)
            }
            MotionEvent.ACTION_DOWN -> {
                axisNo = (axisNo + 1)%3
            }
        }

        invalidate()
        return true
    }

    fun rotate(axisNo: Int) {
        val t: Double = .1

        var v1 = axis1.copy()
        var v2 = axis2.copy()
        var v3 = axis3.copy()
        val cost = Math.cos(t)
        val sint = Math.sin(t)

        when(axisNo) {
            0 -> {
                v2 = axis2 * cost + axis3 * sint
                v3 = axis2 * (-sint) + axis3 * cost

                axis2 = v2
                axis3 = v3
            }
            1 -> {
                v3 = axis3 * cost + axis1 * sint
                v1 = axis3 * (-sint) + axis1 * cost

                axis1 = v1
                axis3 = v3
            }
            2 -> {
                v1 = axis1 * cost + axis2 * sint
                v2 = axis1 * (-sint) + axis2 * cost

                axis1 = v1
                axis2 = v2
            }
        }
    }
}