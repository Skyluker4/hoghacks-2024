import 'dart:async';

import 'package:flutter/material.dart';

import 'package:playpredict/shared/style.dart';
import 'package:playpredict/models/prediction.dart';
import 'package:playpredict/shared/api.dart';

class PredictButton extends StatefulWidget {
  const PredictButton({super.key});

  @override
  State<PredictButton> createState() => _PredictButtonState();
}

class _PredictButtonState extends State<PredictButton> {
  Timer? timer;
  List<Prediction>? predictions;

  @override
  void initState() {
    super.initState();
    _getPredictions();
    timer =
        Timer.periodic(const Duration(seconds: 1), (_) => _getPredictions());
  }

  Future<void> _getPredictions() async {
    final newPredictions = await API.getPredictions();
    setState(() {
      predictions = newPredictions;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width * 0.3,
      padding: const EdgeInsets.all(15),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.primaryContainer,
        border: Border.all(
          color: Theme.of(context).colorScheme.primary,
          width: 3,
        ),
        borderRadius: BorderRadius.circular(8),
      ),
      child: GestureDetector(
        behavior: HitTestBehavior.translucent,
        onTap: () {
          for (final prediction in predictions!) {
            print(prediction.name);
          }
        },
        child: Column(children: [
          const Spacer(),
          const Icon(Icons.sports_football_outlined, size: 192),
          const Spacer(),
          Text(predictions?[0].name ?? 'Waiting...', style: bigText()),
        ]),
      ),
    );
  }
}
