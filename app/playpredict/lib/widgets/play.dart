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
      width: 200,
      decoration: BoxDecoration(
        border: Border.all(color: Colors.black),
        borderRadius: BorderRadius.circular(10),
      ),
      child: const Center(
        child: Text('Play'),
      ),
    );
  }
}
