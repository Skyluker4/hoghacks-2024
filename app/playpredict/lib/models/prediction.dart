/*// ignore_for_file: non_constant_identifier_names

import 'package:json_annotation/json_annotation.dart';

part 'prediction.g.dart';

@JsonSerializable()
class Prediction {
  Prediction({
    required this.id,
    required this.name,
    required this.prediction,
  });

  factory Prediction.fromJson(Map<String, dynamic> json) =>
      _$PredictionFromJson(json);

  final int id;
  final String name;
  final String prediction;

  Map<String, dynamic> toJson() => _$PredictionToJson(this);
}*/
