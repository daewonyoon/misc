package com.oozzuu.kotlin.simplegame

import android.graphics.PointF

data class Vector3D(
    val x: Float,
    val y: Float,
    val z: Float
) {
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
}

data class ProjectionWorld(
    val o: PointF,
    val exx: Float,    val exy: Float,
    val eyx: Float,    val eyy: Float,
    val ezx: Float,    val ezy: Float
) {

    fun setO(o_: PointF): ProjectionWorld {
        return ProjectionWorld(o_, exx, exy, eyx, eyy, ezx, ezy)
    }

    fun setScale(r: Float): ProjectionWorld {
        return ProjectionWorld(o, r * exx, r * exy, r * eyx, r * eyy, r * ezx, r * ezy)
    }

    fun getProjection(v: Vector3D): PointF {
        return PointF(
            o.x + v.x * exx + v.y * eyx + v.z * ezx,
            o.y + v.x * exy + v.y * eyy + v.z * ezy
        )
    }
}