import 'package:flutter/material.dart';

class PlayTile extends StatefulWidget {
  const PlayTile({super.key});

  @override
  State<PlayTile> createState() => _PlayTileState();
}

class _PlayTileState extends State<PlayTile> {
  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(left: 10),
      padding: const EdgeInsets.all(10),
      width: MediaQuery.of(context).size.height * 0.3,
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.primaryContainer,
        border: Border.all(
          color: Theme.of(context).colorScheme.primary,
          width: 3,
        ),
        borderRadius: BorderRadius.circular(10),
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          const Spacer(),
          Icon(
            Icons.sports_football_outlined,
            size: 96,
            color: Theme.of(context).colorScheme.onPrimaryContainer,
          ),
          const Spacer(),
          Text(
            'Play',
            style: TextStyle(
              color: Theme.of(context).colorScheme.onPrimaryContainer,
              fontSize: 24,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }
}
