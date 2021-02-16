package com.oozzuu.drawshape

data class Vector3D(
    val x: Float,
    val y: Float,
    val z: Float
)

operator fun Vector3D.unaryMinus() = Vector3D(-x, -y, -z)
operator fun Vector3D.plus(other: Vector3D) = Vector3D(x + other.x,y + other.y,z + other.z)
operator fun Vector3D.minus(other: Vector3D) = this + (-other)
fun Vector3D.dot(other: Vector3D) : Float = x*other.x + y*other.y + z*other.z
fun Vector3D.cross(other: Vector3D) : Vector3D {
    val zz : Float = x * other.y - y * other.x
    val xx : Float = y * other.z - z * other.y
    val yy : Float = z * other.x - x * other.z
    return Vector3D(xx, yy, zz)
}

