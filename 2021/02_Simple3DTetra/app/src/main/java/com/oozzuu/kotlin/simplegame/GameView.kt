package com.oozzuu.kotlin.simplegame

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.view.MotionEvent
import android.view.View

class GameView(context: Context) : View(context) {

    val paint: Paint

    var o: Vector3D
    var axis1: Vector3D
    var axis2: Vector3D
    var axis3: Vector3D
    var axisNo: Int = 0

    var canvas_ox: Float
    var canvas_oy: Float

    init {
        paint = Paint()
        paint.isFilterBitmap = true
        paint.isAntiAlias = true
        paint.strokeWidth = 4f
        paint.color = Color.BLUE

        canvas_ox = 500f
        canvas_oy = 500f

        o = Vector3D(0f, 0f, 0f).setO(canvas_ox, canvas_oy)
        axis1 = Vector3D(1f, 0f, 0f).setO(canvas_ox, canvas_oy)
        axis2 = Vector3D(0f, 1f, 0f).setO(canvas_ox, canvas_oy)
        axis3 = Vector3D(0f, 0f, 1f).setO(canvas_ox, canvas_oy)
    }

    override fun draw(canvas: Canvas?) {
        super.draw(canvas)
        canvas?.drawColor(Color.WHITE)
        drawTetraHadra(canvas)
    }

    fun drawTetraHadra(canvas: Canvas?) {
        val w: Float = 4f

        drawLine(canvas, axis1, axis2, Color.BLUE, w)
        drawLine(canvas, axis2, axis3, Color.MAGENTA, w)
        drawLine(canvas, axis3, axis1, Color.LTGRAY, w)

        drawLine(canvas, o, axis1, Color.GREEN, if (axisNo == 0) w * 3 else w)
        drawLine(canvas, o, axis2, Color.RED, if (axisNo == 1) w * 3 else w)
        drawLine(canvas, o, axis3, Color.BLACK, if (axisNo == 2) w * 3 else w)
    }

    fun drawLine(canvas: Canvas?, x1: Float, y1: Float, x2: Float, y2: Float, col: Int, width: Float = 4f) {
        paint.color = col
        paint.strokeWidth = width
        canvas?.drawLine(x1, y1, x2, y2, paint)
    }

    fun drawLine(canvas: Canvas?, v1:Vector3D, v2:Vector3D, col: Int, width: Float = 4f) {
        paint.color = col
        paint.strokeWidth = width
        canvas?.drawLine(v1.x_prj, v1.y_prj, v2.x_prj, v2.y_prj, paint)
    }

    override fun onTouchEvent(event: MotionEvent): Boolean {
        when (event.action) {
            MotionEvent.ACTION_MOVE -> {
                rotate(axisNo)
            }
            MotionEvent.ACTION_DOWN -> {
                axisNo = (axisNo + 1) % 3
            }
        }

        invalidate()
        return true
    }

    fun rotate(axisNo: Int) {
        val t: Double = .2

        var v1 = axis1.copy()
        var v2 = axis2.copy()
        var v3 = axis3.copy()
        val cost = Math.cos(t)
        val sint = Math.sin(t)

        when (axisNo) {
            0 -> {
                v2 = axis2 * cost + axis3 * sint
                v3 = axis2 * (-sint) + axis3 * cost

                axis2 = v2
                axis3 = v3
            }
            1 -> {
                v3 = axis3 * cost + axis1 * sint
                v1 = axis3 * (-sint) + axis1 * cost

                axis3 = v3
                axis1 = v1
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