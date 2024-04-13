import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

import 'package:playpredict/models/prediction.dart';
import 'package:playpredict/shared/style.dart';
import 'package:playpredict/shared/api.dart';

class PredictionTile extends StatefulWidget {
  const PredictionTile(
      {super.key,
      required this.prediction,
      required this.onTap,
      required this.selected});

  final Prediction prediction;
  final void Function() onTap;
  final bool selected;

  @override
  State<PredictionTile> createState() => _PredictionTileState();
}

class _PredictionTileState extends State<PredictionTile> {
  String? imageURL;

  @override
  void initState() {
    super.initState();
    imageURL = API.getImageURL(widget.prediction.image);
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(10),
      height: MediaQuery.of(context).size.height * 0.28,
      decoration: BoxDecoration(
        color: widget.selected
            ? Theme.of(context).colorScheme.primary
            : Theme.of(context).colorScheme.primaryContainer,
        border: Border.all(
          color: Theme.of(context).colorScheme.primary,
          width: 3,
        ),
        borderRadius: BorderRadius.circular(10),
      ),
      child: GestureDetector(
        behavior: HitTestBehavior.translucent,
        onTap: widget.onTap,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Expanded(
              child: imageURL != null
                  ? SvgPicture.network(imageURL!)
                  : const Icon(Icons.sports_football_outlined, size: 96),
            ),
            Text(widget.prediction.name, style: smallText()),
          ],
        ),
      ),
    );
  }
}
