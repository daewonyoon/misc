package com.oozzuu.kotlin.simplegame

data class Vector3D(
    val x: Float,
    val y: Float,
    val z: Float
)
{
    operator fun times(r: Double): Vector3D {
        val rr :Float = r.toFloat()
        return Vector3D(rr*x, rr*y, rr*z)
    }

    operator fun plus(v: Vector3D): Vector3D {
        return Vector3D( x+v.x, y+v.y, z+v.z)
    }

    var ox:Float = 500f
    var oy:Float = 500f
    var exx:Float = 400f
    var exy:Float = 0f
    var eyx:Float = -80f
    var eyy:Float = 320f
    var ezx:Float = -80f
    var ezy:Float = -320f

    var x_prj:Float = 0.0f
        get() {
            return ox+x*exx + y*eyx + z*ezx
        }

    var y_prj:Float = 0.0f
        get() {
            return oy+x*exy + y*eyy + z*ezy
        }


}
