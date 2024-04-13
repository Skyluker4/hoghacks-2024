import 'package:flutter/material.dart';
import 'dart:async';

import 'package:playpredict/widgets/play_tile.dart';
import 'package:playpredict/widgets/predict_button.dart';
import 'package:playpredict/shared/style.dart';
import 'package:playpredict/models/situation.dart';
import 'package:playpredict/shared/api.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  Timer? timer;
  Situation? situation;

  @override
  void initState() {
    super.initState();
    _getSituation();
    timer = Timer.periodic(const Duration(seconds: 1), (_) => _getSituation());
  }

  Future<void> _getSituation() async {
    final newSituation = await API.getSituation();
    setState(() {
      situation = newSituation;
    });
  }

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
                        _bigData('Quarter', _getQuarter()),
                        const Spacer(),
                        _bigData('Down', _getDown()),
                      ],
                    ),
                    Column(
                      children: [
                        _bigData('Time', situation?.time ?? 'N/A'),
                        const Spacer(),
                        _bigData('Yard Line', _getYardage()),
                      ],
                    ),
                    const PredictButton(),
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

  String _getQuarter() {
    if (situation == null) {
      return 'N/A';
    }
    switch (situation!.quarter) {
      case 1:
        return '1st';
      case 2:
        return '2nd';
      case 3:
        return '3rd';
      case 4:
        return '4th';
      default:
        return 'N/A';
    }
  }

  String _getDown() {
    if (situation == null) {
      return 'N/A';
    }
    String down;
    switch (situation!.position.down) {
      case 1:
        down = '1st';
        break;
      case 2:
        down = '2nd';
        break;
      case 3:
        down = '3rd';
        break;
      case 4:
        down = '4th';
        break;
      default:
        down = 'N/A';
    }
    return '$down & ${situation!.position.distance}';
  }

  String _getYardage() {
    if (situation == null) {
      return 'N/A';
    }
    if (situation!.position.yard.isNegative) {
      return 'Away ${situation!.position.yard.abs()}';
    } else {
      return 'Home ${situation!.position.yard}';
    }
  }

  @override
  void dispose() {
    timer?.cancel();
    super.dispose();
  }
}
