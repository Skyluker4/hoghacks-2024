import 'package:flutter/material.dart';

import 'package:playpredict/shared/style.dart';

class PredictButton extends StatefulWidget {
  const PredictButton({super.key});

  @override
  State<PredictButton> createState() => _PredictButtonState();
}

class _PredictButtonState extends State<PredictButton> {
  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width * 0.3,
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
          print('Predict');
        },
        child: Center(
          child: Text('Predict', style: bigText()),
        ),
      ),
    );
  }
}
