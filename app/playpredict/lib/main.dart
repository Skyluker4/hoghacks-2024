import 'package:flutter/material.dart';

import 'package:playpredict/home.dart';

Future<void> main() async {
  runApp(const PlayPredict());
}

class PlayPredict extends StatelessWidget {
  const PlayPredict({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const Home(),
    );
  }
}
