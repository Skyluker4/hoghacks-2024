// ignore_for_file: non_constant_identifier_names

import 'package:json_annotation/json_annotation.dart';

part 'situation.g.dart';

@JsonSerializable()
class Situation {
  final int away_score;
  final int home_score;
  final bool is_possessing_team;
  final Position position;
  final int quarter;
  final String time;

  Situation({
    required this.away_score,
    required this.home_score,
    required this.is_possessing_team,
    required this.position,
    required this.quarter,
    required this.time,
  });

  factory Situation.fromJson(Map<String, dynamic> json) =>
      _$SituationFromJson(json);

  Map<String, dynamic> toJson() => _$SituationToJson(this);
}

@JsonSerializable()
class Position {
  final int distance;
  final int down;

  final int yard;

  Position({
    required this.distance,
    required this.down,
    required this.yard,
  });

  factory Position.fromJson(Map<String, dynamic> json) =>
      _$PositionFromJson(json);

  Map<String, dynamic> toJson() => _$PositionToJson(this);
}
