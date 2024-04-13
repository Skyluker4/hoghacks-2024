// ignore_for_file: non_constant_identifier_names

import 'package:json_annotation/json_annotation.dart';

part 'prediction.g.dart';

@JsonSerializable()
class Prediction {
  Prediction({
    required this.formation,
    required this.image,
    required this.name,
    required this.weight,
  });

  factory Prediction.fromJson(Map<String, dynamic> json) =>
      _$PredictionFromJson(json);

  final String formation;
  final String image;
  final String name;
  final double weight;

  Map<String, dynamic> toJson() => _$PredictionToJson(this);
}
