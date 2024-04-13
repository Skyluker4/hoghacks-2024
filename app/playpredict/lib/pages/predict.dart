import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

import 'package:playpredict/models/prediction.dart';
import 'package:playpredict/shared/api.dart';
import 'package:playpredict/shared/style.dart';
import 'package:playpredict/widgets/predict_tile.dart';

class PredictionPage extends StatefulWidget {
  const PredictionPage({super.key, required this.predictions});

  final List<Prediction> predictions;

  @override
  State<PredictionPage> createState() => _PredictionPageState();
}

class _PredictionPageState extends State<PredictionPage> {
  int selectedPrediction = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Row(
          children: [
            _predList(),
            _divider(0),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(0, 2, 10, 2),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    _bigPicture(),
                    _bigButton(),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _predList() {
    return SizedBox(
      width: MediaQuery.of(context).size.width * 0.3,
      child: ListView.separated(
        padding: const EdgeInsets.fromLTRB(10, 2, 0, 2),
        itemCount: widget.predictions.length,
        itemBuilder: (context, index) {
          final prediction = widget.predictions[index];
          return PredictionTile(
              prediction: prediction,
              onTap: () => _selectPrediction(index),
              selected: index == selectedPrediction);
        },
        separatorBuilder: (context, index) => const SizedBox(height: 10),
      ),
    );
  }

  void _selectPrediction(int index) {
    setState(() {
      selectedPrediction = index;
    });
  }

  Widget _divider(double indent) {
    return VerticalDivider(
      color: Theme.of(context).colorScheme.primary,
      thickness: 3,
      indent: indent,
      endIndent: indent,
    );
  }

  Widget _bigButton() {
    return Container(
      height: MediaQuery.of(context).size.height * 0.3,
      padding: const EdgeInsets.fromLTRB(0, 0, 10, 2),
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
          Navigator.pop(context);
        },
        child: Center(
          child: Text(_buttonText(), style: bigText()),
        ),
      ),
    );
  }

  String _buttonText() {
    return 'Select ${widget.predictions[selectedPrediction].name}';
  }

  Widget _bigPicture() {
    final prediction = widget.predictions[selectedPrediction];
    final imageURL = API.getImageURL(prediction.image);

    return Expanded(
      child: imageURL != null
          ? SvgPicture.network(imageURL)
          : const Icon(Icons.sports_football_outlined, size: 256),
    );
  }
}
