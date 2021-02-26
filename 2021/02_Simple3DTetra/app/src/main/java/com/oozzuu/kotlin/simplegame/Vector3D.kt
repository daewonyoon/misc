package com.oozzuu.kotlin.simplegame

data class Vector3D(
    val x: Float,
    val y: Float,
    val z: Float
) {

    constructor(_x:Float, _y:Float, _z:Float, _ox:Float, _oy:Float): this(_x, _y, _z) {
        setO(_ox, _oy)
    }
    operator fun times(r: Double): Vector3D {
        val rr: Float = r.toFloat()
        return Vector3D(rr * x, rr * y, rr * z)
    }

    operator fun plus(v: Vector3D): Vector3D {
        return Vector3D(x + v.x, y + v.y, z + v.z)
    }

    fun dot(v: Vector3D): Float {
        return x * v.x + y * v.y + z * v.z
    }

    fun cross(v: Vector3D): Vector3D {
        val xx: Float = y * v.z - z * v.y
        val yy: Float = z * v.x - x * v.z
        val zz: Float = x * v.y - y * v.y

        return Vector3D(xx, yy, zz)
    }

    var ox: Float = 500f
    var oy: Float = 500f
    var exx: Float = 400f
    var exy: Float = 0f
    var eyx: Float = -80f
    var eyy: Float = 320f
    var ezx: Float = -100f
    var ezy: Float = -280f

    var x_prj: Float = 0.0f
        get() {
            return ox + x * exx + y * eyx + z * ezx
        }

    var y_prj: Float = 0.0f
        get() {
            return oy + x * exy + y * eyy + z * ezy
        }

    fun setO(ox: Float, oy: Float): Vector3D {
        this.ox = ox
        this.oy = oy
        return this
    }
}
