/*// ignore_for_file: non_constant_identifier_names

import 'package:json_annotation/json_annotation.dart';

part 'formation.g.dart';

@JsonSerializable()
class Formation {
  Formation({
    required this.id,
    required this.name,
    required this.formation,
  });

  factory Formation.fromJson(Map<String, dynamic> json) =>
      _$FormationFromJson(json);

  final int id;
  final String name;
  final String formation;

  Map<String, dynamic> toJson() => _$FormationToJson(this);
}*/
