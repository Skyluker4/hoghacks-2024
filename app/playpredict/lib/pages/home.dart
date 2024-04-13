import 'package:flutter/material.dart';

import 'package:playpredict/widgets/play_tile.dart';
import 'package:playpredict/widgets/predict_button.dart';
import 'package:playpredict/shared/style.dart';

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
            _playList(),
            _divider(8),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 8),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Column(
                      children: [
                        _bigData('Quarter', '1st'),
                        const Spacer(),
                        _bigData('Down', '1st & 10'),
                      ],
                    ),
                    Column(
                      children: [
                        _bigData('Time', '15:00'),
                        const Spacer(),
                        _bigData('Yard Line', '50'),
                      ],
                    ),
                    PredictButton(),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _playList() {
    return SizedBox(
      height: MediaQuery.of(context).size.height * 0.3,
      child: ListView(
        scrollDirection: Axis.horizontal,
        children: const [
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
    );
  }

  Widget _bigData(String title, String data) {
    return Column(
      children: [
        Text(title, style: bigText()),
        Text(data, style: hugeText()),
      ],
    );
  }

  Widget _divider(double indent) {
    return Divider(
      color: Theme.of(context).colorScheme.primary,
      thickness: 2,
      indent: indent,
      endIndent: indent,
    );
  }
}
