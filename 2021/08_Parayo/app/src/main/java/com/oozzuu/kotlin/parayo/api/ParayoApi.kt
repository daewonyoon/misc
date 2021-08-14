package com.oozzuu.kotlin.parayo.api

import com.oozzuu.kotlin.parayo.api.response.ApiResponse
import retrofit2.http.GET

interface ParayoApi {

    @GET("/api/v1/hello")
    suspend fun hello(): ApiResponse<String>

    companion object {
        val instance = ApiGenerator().generate(ParayoApi::class.java)
    }

}