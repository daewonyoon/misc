package com.oozzuu.kotlin.simplegame

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.PointF
import android.view.MotionEvent
import android.view.View
import androidx.core.view.MotionEventCompat

class GameView(context: Context) : View(context) {

    private var mActivePointerId: Int = 0
    private var mLastTouchX: Float = 0f
    private var mLastTouchY: Float = 0f
    private val paint: Paint

    private var o: Vector3D
    private var axis1: Vector3D
    private var axis2: Vector3D
    private var axis3: Vector3D
    private var axisNo: Int = 0

    private var canvas_o: PointF
    private var canvas_o_cache: PointF = PointF(0f, 0f)
    private var projectionworld: ProjectionWorld

    private var is_moving: Boolean = false

    init {
        paint = Paint()
        paint.isFilterBitmap = true
        paint.isAntiAlias = true
        paint.strokeWidth = 4f
        paint.color = Color.BLUE

        canvas_o = PointF(500f, 1000f)
        projectionworld = ProjectionWorld(
            canvas_o,
            400f, 0f,
            -80f, 320f,
            -100f, -280f
        )

        o = Vector3D(0f, 0f, 0f)
        axis1 = Vector3D(1f, 0f, 0f)
        axis2 = Vector3D(0f, 1f, 0f)
        axis3 = Vector3D(0f, 0f, 1f)
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


    fun drawLine(canvas: Canvas?, v1: Vector3D, v2: Vector3D, col: Int, width: Float = 4f) {
        var p1: PointF = projectionworld.getProjection(v1)
        var p2: PointF = projectionworld.getProjection(v2)
        paint.color = col
        paint.strokeWidth = width
        canvas?.drawLine(p1.x, p1.y, p2.x, p2.y, paint)
    }

    fun isNearOrg(x: Float, y: Float): Boolean {
        return Math.abs(x - canvas_o.x) < 10f && Math.abs(y - canvas_o.y) < 10f
    }

    fun move_canvas_o() {
        projectionworld = projectionworld.setO(canvas_o)
    }

    override fun onTouchEvent(event: MotionEvent): Boolean {
        when (event.action) {
            MotionEvent.ACTION_MOVE -> {
                if (is_moving) {
                    val (x: Float, y: Float) =
                        MotionEventCompat.findPointerIndex(event, mActivePointerId)
                            .let { pointerIndex ->
                                // Calculate the distance moved
                                MotionEventCompat.getX(event, pointerIndex) to
                                    MotionEventCompat.getY(event, pointerIndex)
                            }

                    canvas_o.x = canvas_o_cache.x + x - mLastTouchX
                    canvas_o.y = canvas_o_cache.y + y - mLastTouchY
                    move_canvas_o()
                } else {
                    rotate(axisNo)
                }
            }
            MotionEvent.ACTION_DOWN -> {
                var x: Float = 0f
                var y: Float = 0f
                MotionEventCompat.getActionIndex(event).also { pointerIndex ->
                    // Remember where we started (for dragging)
                    x = MotionEventCompat.getX(event, pointerIndex)
                    y = MotionEventCompat.getY(event, pointerIndex)
                }
                if (isNearOrg(x, y)) {
                    is_moving = true

                    mLastTouchX = x
                    mLastTouchY = y
                    canvas_o_cache.x = canvas_o.x
                    canvas_o_cache.y = canvas_o.y

                    // Save the ID of this pointer (for dragging)
                    mActivePointerId = MotionEventCompat.getPointerId(event, 0)
                } else {
                    axisNo = (axisNo + 1) % 3
                }
            }

            MotionEvent.ACTION_UP -> {
                if (is_moving) {
                    is_moving = false
                }
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