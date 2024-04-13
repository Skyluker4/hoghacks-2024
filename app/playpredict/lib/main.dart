import 'package:flutter/material.dart';

import 'package:playpredict/pages/home.dart';

Future<void> main() async {
  runApp(const PlayPredict());
}

class PlayPredict extends StatelessWidget {
  const PlayPredict({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          brightness: Brightness.light,
          seedColor: Colors.green,
        ),
        useMaterial3: true,
      ),
      darkTheme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          brightness: Brightness.dark,
          seedColor: Colors.green,
        ),
        useMaterial3: true,
      ),
      home: const Home(),
    );
  }
}
