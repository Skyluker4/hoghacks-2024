import 'package:flutter/material.dart';

import 'package:playpredict/widgets/play.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            SizedBox(
              height: MediaQuery.of(context).size.height * 0.3,
              child: ListView(
                scrollDirection: Axis.horizontal,
                children: [
                  PlayTile(),
                  PlayTile(),
                  PlayTile(),
                  PlayTile(),
                  PlayTile(),
                  PlayTile(),
                  PlayTile(),
                  PlayTile(),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
