package com.example.dfms

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.dfms.ui.HomeScreen
import com.example.dfms.ui.LoginScreen
import com.example.dfms.ui.SignupScreen

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MyApp()
        }
    }
}

@Composable
fun MyApp() {
    MaterialTheme {
        Surface {
            MyAppNavHost()
        }
    }
}

@Composable
fun MyAppNavHost() {
    val navController: NavHostController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = "login" // Start with LoginScreen
    ) {
        composable("login") { LoginScreen(navController) }
        composable("home") { HomeScreen(navController) } // Add HomeScreen to the navigation graph
    }
}
