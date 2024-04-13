import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

import 'package:playpredict/models/formation.dart';
import 'package:playpredict/shared/style.dart';
import 'package:playpredict/shared/api.dart';

class PlayTile extends StatefulWidget {
  const PlayTile({super.key, required this.formation});

  final Formation formation;

  @override
  State<PlayTile> createState() => _PlayTileState();
}

class _PlayTileState extends State<PlayTile> {
  String? imageURL;

  @override
  void initState() {
    super.initState();
    imageURL = API.getImageURL(widget.formation.image);
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(10),
      width: MediaQuery.of(context).size.width * 0.25,
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.primaryContainer,
        border: Border.all(
          color: Theme.of(context).colorScheme.primary,
          width: 3,
        ),
        borderRadius: BorderRadius.circular(10),
      ),
      child: GestureDetector(
        behavior: HitTestBehavior.translucent,
        onTap: () {
          print(widget.formation.name);
        },
        child: Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Expanded(
              child: imageURL != null
                  ? SvgPicture.network(imageURL!)
                  : const Icon(Icons.sports_football_outlined, size: 96),
            ),
            Text(widget.formation.name, style: smallText()),
          ],
        ),
      ),
    );
  }
}
