package com.oozzuu.kotlin.parayo.api.response

data class ApiResponse<T>(
    val success: Boolean,
    val data: T? = null,
    val message: String? = null
) {
    companion object {
        inline fun <reified T> error(message: String? = null) =
            ApiResponse(false, null as T?, message)
    }
}